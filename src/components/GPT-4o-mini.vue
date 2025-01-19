<template>
  <input type="text" v-model="inputQuestion">
  <button @click="quickChat(inputQuestion)">点我发送</button>
  <textarea>{{ response }}</textarea>
</template>


<script setup lang="ts">
  // import invokeLLM from '@/service/llmService'
  import { ref } from 'vue'

  const response = ref('')
  const inputQuestion = ref('')

  async function quickChat(inputQuestion:string) {
    try {
      const res = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: inputQuestion }),
      });

      if (!res.ok) {
        throw new Error('网络响应不正常');
      }

      const data = await res.json();
      console.log(data)
      response.value = data.response; // 更新响应内容
      console.log(data.response);
    } catch (error) {
      console.error('调用接口失败:', error);
      response.value = '调用失败，请检查控制台日志。';
    }
  }
</script>


<style scoped>
  textarea{
    width: 500px;
    height: 500px;
    border: 1px solid red;
    margin: 20px;
  }
</style>
