#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai/">
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png" width="200" align="center">
# </a>
# 
# <h1 align="center"><font size="5"><b>Application Programming Interface</b></font></h1>

# <p>In this notebook, you will learn to convert an audio file of an English speaker to text using a Speech to Text API. Then you will translate the English version to a Spanish version using a Language Translator API. <b>Note:</b> You must obtain the API keys and enpoints to complete the lab.</p>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/topNotebooksPython101Coursera">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png" width="750" align="center">
#     </a>
# </div>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <h2>Table of Contents</h2>
# <ul>
#     <li><a href="#ref0">Speech To Text</a></li>
#     <li><a href="#ref1">Language Translator</a></li>
#     <li><a href="#ref2">Exercise</a></li>
# </ul>
# <br>
# <p>Estimated Time Needed: <strong>25 min</strong></p>
# </div>

# In[36]:


#you will need the following library 
get_ipython().system('pip install ibm_watson wget')


# <h2 id="ref0">Speech to Text</h2>

# <p>First we import <code>SpeechToTextV1</code> from <code>ibm_watson</code>.For more information on the API, please click on this <a href="https://cloud.ibm.com/apidocs/speech-to-text?code=python">link</a></p>

# In[37]:


from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# <p>The service endpoint is based on the location of the service instance, we store the information in the variable URL. To find out which URL to use, view the service credentials.</p>

# In[38]:


url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"


# <p>You require an API key, and you can obtain the key on the <a href="https://cloud.ibm.com/resources">Dashboard </a>.</p>

# In[40]:


iam_apikey_s2t = '3gVyV0YxVah5MY6vS5zbKX7JQmxxtd6M44hUT-Yv-aG6'


# <p>You create a <a href="http://watson-developer-cloud.github.io/python-sdk/v0.25.0/apis/watson_developer_cloud.speech_to_text_v1.html">Speech To Text Adapter object</a> the parameters are the  endpoint and API key.</p>

# In[41]:


authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t


# <p>Lets download the audio file that we will use to convert into text.</p>

# In[45]:


Users(/kevilkhadka/wget, -O, PolynomialRegressionandPipelines.mp3, https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3)
    


# <p>We have the path of the wav file we would like to convert to text</p>

# In[ ]:


filename='PolynomialRegressionandPipelines.mp3'


# <p>We create the file object <code>wav</code> with the wav file using  <code>open</code> ; we set the <code>mode</code> to  "rb" ,  this is similar to read mode, but it ensures the file is in binary mode.We use the method <code>recognize</code> to return the recognized text. The parameter audio is the file object <code>wav</code>, the parameter <code>content_type</code> is the format of the audio file.</p>

# In[43]:


with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')


# <p>The attribute result contains a dictionary that includes the translation:</p>

# In[ ]:


response.result


# In[ ]:


from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")


# In[ ]:


response


# <p>We can obtain the recognized text and assign it to the variable <code>recognized_text</code>:</p>

# In[ ]:


recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)


# <h2 id="ref1">Language Translator</h2>

# <p>First we import <code>LanguageTranslatorV3</code> from ibm_watson. For more information on the API click <a href="https://cloud.ibm.com/apidocs/speech-to-text?code=python"> here</a></p>

# In[16]:


from ibm_watson import LanguageTranslatorV3


# <p>The service endpoint is based on the location of the service instance, we store the information in the variable URL. To find out which URL to use, view the service credentials.</p>

# In[17]:


url_lt='https://gateway.watsonplatform.net/language-translator/api'


# <p>You require an API key, and you can obtain the key on the <a href="https://cloud.ibm.com/resources">Dashboard</a>.</p>

# In[18]:


apikey_lt="goyNzZU1G0YFteGA-SXzFAwZvy4WoO9zvs5d-Vj1Qjth"


# <p>API requests require a version parameter that takes a date in the format version=YYYY-MM-DD. This lab describes the current version of Language Translator, 2018-05-01</p>

# In[19]:


version_lt='2018-05-01'


# <p>we create a  Language Translator object <code>language_translator</code>:</p>

# In[20]:


authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator


# <p>We can get a Lists the languages that the service can identify.
# The method Returns the language code.  For example English (en) to  Spanis (es) and name of each language.</p>

# In[21]:


from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


# <p>We can use the method <code>translate</code> this will translate the text. The parameter text is the text. Model_id is the type of model we would like to use use we use list the the langwich . In this case, we set it to 'en-es' or English to Spanish. We get a Detailed Response object translation_response</p>

# In[22]:


translation_response = language_translator.translate(    text=recognized_text, model_id='en-es')
translation_response


# <p>The result is a dictionary.</p>

# In[23]:


translation=translation_response.get_result()
translation


# <p>We can obtain the actual translation as a string as follows:</p>

# In[24]:


spanish_translation =translation['translations'][0]['translation']
spanish_translation 


# <p>We can translate back to English</p>

# In[25]:


translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()


# <p>We can obtain the actual translation as a string as follows:</p>

# In[26]:


translation_eng=translation_new['translations'][0]['translation']
translation_eng


# <p>We can convert it to french as well:</p>

# In[27]:


French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()


# In[28]:


French_translation['translations'][0]['translation']


# <h3>Language Translator</h3>

#  <a href="http://cocl.us/NotebooksPython101bottom"><img src="https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width="750" align="center"></a>

# <b>References</b>

# https://cloud.ibm.com/apidocs/speech-to-text?code=python

# https://cloud.ibm.com/apidocs/language-translator?code=python

# <hr>

# <h4>About the Author:</h4>
# <p><a href="https://www.linkedin.com/in/joseph-s-50398b136/">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>

# Other contributor: <a href="https://www.linkedin.com/in/fanjiang0619/">Fan Jiang</a>

# Copyright &copy; 2019 [cognitiveclass.ai](https:cognitiveclass.ai). This notebook and its source code are released under the terms of the [MIT License](cognitiveclass.ai).
