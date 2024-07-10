from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Using local model with agents
from langchain_community.llms import Ollama
import os

# os.environ["OPENAI_API_BASE"] = "http://localhost:1234/v1"
# os.environ["OPENAI_API_KEY"] = "lm-studio"

ollama_model = 'http://localhost:11434'

os.environ["OPENAI_API_BASE"] = ollama_model
os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
os.environ["OPENAI_API_KEY"] = "sk-111111111111111111111111111111111111111111111111"
# Uncomment the following line to use an example of a custom tool
from cybercrew.tools.thehive_tool import TheHiveAlertsTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CyberSecCrew():
	"""CyberSecCrew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	def __init__(self) -> None:
		self.ollama_llm = Ollama(model = "openhermes", base_url = "http://localhost:11434")
		

	@agent
	def soc_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['soc_manager'],
			tools=[TheHiveAlertsTool()], # Example of custom tool, loaded on the beginning of file
			llm=self.ollama_llm
		)

	@agent
	def triage_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['triage_specialist'],
   			tools=[TheHiveAlertsTool()],
 			llm=self.ollama_llm
		)
  
	@agent
	def senior_soc_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['senior_soc_analyst'],
			llm=self.ollama_llm
		)

	@agent
	def threat_intell(self) -> Agent:
		return Agent(
			config=self.agents_config['threat_intell'],
   			llm=self.ollama_llm
		)

	@task
	def tk_thehive_input(self) -> Task:
		return Task(
			config=self.tasks_config['tk_thehive_input'],
			agent=self.triage_specialist()
		)

	@task
	def tk_triage_alerts(self) -> Task:
		return Task(
			config=self.tasks_config['tk_triage_alerts'],
			agent=self.triage_specialist()
		)

	@task
	def tk_triage_review(self) -> Task:
		return Task(
			config=self.tasks_config['tk_triage_review'],
			agent=self.senior_soc_analyst(),
			output_file='cyber_analyst_report.md'
		)

	@task
	def tk_write_report(self) -> Task:
		return Task(
			config=self.tasks_config['tk_write_report'],
			agent=self.threat_intell(),
			output_file='cyber_report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CyberCrew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
   			manager_agent=self.soc_manager(),
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)