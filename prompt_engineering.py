import json

EDUCATION_PROMPT = "prompt"

SKILLS_PROMPT = ""

PREVIOUS_EXPERIENCE_PROMPT = ""

def engineering_prompt(resume, job_description, section):
  """ Produce a prompt for an LLM to generate a resume section that matches the given job description"""
  prompt = "Given the following resume: " + resume 
  if section == "Education":
    prompt += "Write an Education section that includes the degree type, B.S., M.S. as well as the university, the years they attended, and the location of that university" 
  elif section == "Skills":
    prompt += "Edit the skills section to more closely match this job description: " + job_description
  elif section == "Professional Experience":
    prompt += "Edit the professional experience to align more closely with this job description" + job_description + " using the STAR method" 
  elif section == "Projects":
    prompt += "Edit the project descriptions to match the responsibilities of the job section more closely. Where the job description is: " + job_description

  #check 1024 word count ?
  words = prompt.split()
  # Take the first max_words words
  truncated_words = words[:1000]
  # Join the words back into a string
  truncated_prompt = ' '.join(truncated_words)

  return truncated_prompt