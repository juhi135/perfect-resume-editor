
def engineering_prompt(resume, job_description, section):
  """ Produce a prompt for an LLM to generate a resume section that matches the given job description"""
  prompt = "Temorary prompt"
  if section == "Education":
    prompt = """
        Given the following resume: """+ resume + """. Generate an education section in the format
        - university/college 
        - location 
        - Degree and Degree type 
        - start - end date
        - GPA if included

        To best match this job description:
        """ + job_description

  elif section == "Skills":
    prompt = """
        Given the following resume: """ + resume + """. Generate a skills section in the which are
        most relevant according to the job description: """ + job_description + """. Don't add 
        skills which are not in the resume, pick skills from the work experience in the
        resume section as well as from the projects. Focus on a top few set of skills.
        Write it modeled after a good skills section.
        """


  elif section == "Professional Experience":
    prompt = """
        Given the following resume: """+ resume + """. Generate a Professional experience section that
        includes the experiences of the resume in the format
        - company- position
        - start - end date
        - location
        - summary
        The summary section should contain bullet points for what the person did during
        the job. It should follow the STAR method. Highlight specific experiences and tailor
        to match the following job description: """ + job_description



  elif section == "Projects":
    prompt = """
      Given the following resume: """ + resume + """. Generate a Projects section in the following format
      - Project Name
      - Project start and end date
      - explanation
      The explanation section should be done so that skills used in the project and project
      accomplishments are highlighted. Only include projects from the resume. Use
      an active voice, be gramatically correct, use correct spellings. Tailor this 
      section to best fit the following job description: """ + job_description
    

  return prompt