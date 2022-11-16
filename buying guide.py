import requests, base64
import os
import openai
import dotenv
dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

url = "https://localhost/wordpress/wp-json/wp/v2/posts"
wp_user = "automationtest"
wp_pass = os.getenv("wp_pass")
credintial = f"{wp_user}:{wp_pass}"
wp_token = base64.b64encode(credintial.encode())
wp_header = {"Authorization":f"Basic {wp_token.decode('utf-8')}"}


def wp_h2(text):
  '''
  This function generate heading 2 html code for wordpress
  :param text:
  :return: html code for gutenberg code editor
  '''
  codes = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
  return codes


def wp_paragraph(text):
  '''
  This function is for generating wp paragraph.
  :param text:
  :return: html code for gutenberg code editor
  '''
  codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
  return codes



file = open('keyword for buying guide.txt')
keywords = file.readlines()
file.close()

for keyword in keywords:
  keyword = keyword.lower().strip('best').strip('top')
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"write 150 words about {keyword}",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
  intro = response.get('choices')[0].get('text')
  wp_intro = wp_paragraph(intro)

  #all paragraph of the content
  first_heading = f'Why {keyword} is important?'
  second_heading = f"How to choose best {keyword}?"
  third_heading = 'What features should be considered?'

  wp_first_heading = wp_h2(first_heading)
  wp_second_heading = wp_h2(second_heading)
  wp_third_heading = wp_h2(third_heading)


  #Why {keyword} is important?
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Why best {keyword} is important? write a list",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
  content_important = response.get('choices')[0].get('text')
  wp_para1 = wp_paragraph(content_important)

  #how to choose best {keyword}
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"how to choose best {keyword}? write 100 words",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
  content_choose_best = response.get('choices')[0].get('text')
  wp_para2 = wp_paragraph(content_choose_best)


  #what features should be considered while buying
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"what features should be considered while buying {keyword}? write a list and guide",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
  content_featurese_considered = response.get('choices')[0].get('text')
  wp_para3 = wp_paragraph(content_featurese_considered)


  #content conclusion
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"write 100 words conclution for buying a {keyword}",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
  content_conclusion = response.get('choices')[0].get('text')
  wp_conclusion = wp_paragraph(content_conclusion)

  content = f'{wp_intro}{wp_first_heading}{wp_para1}{wp_second_heading}{wp_para2}{wp_third_heading}{wp_para3}{wp_conclusion}'

  #post to wordpress
  title = f"{keyword} buying guide"
  slug = title.strip().replace(" ","-")
  post_data = {
      "title": title.title(),
      "content": content,
      "slug": slug
  }

  res = requests.post(url,data=post_data,headers=wp_header,verify=False)
  if res.status_code == 201:
    print("post success")
