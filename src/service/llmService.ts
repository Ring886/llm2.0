// services/llmService.js
import axios from 'axios'
// import 'dotenv/config'

const invokeLLM = async (message) => {
  const config = {
    method: 'post',
    baseURL: 'https://api2.aigcbest.top',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer sk-igzJkocZvGiw0AfnQT3zyrjOCLDC6FfCkbTPd274UDcJiCRO',
    },
    data: {
      model: 'gpt-4o-mini',
      messages: [{ role: 'user', content: message }],
      temperature: 0.7,
    },
  };

  const response = await axios(config);
  console.log(response);

  return response.data.choices[0].message.content;
};

export default invokeLLM;
