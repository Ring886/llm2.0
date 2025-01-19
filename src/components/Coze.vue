<template>
  <div>
    <button @click="quickChat()">点我发送</button>
  </div>
</template>


<script setup lang="ts">
  import { CozeAPI, COZE_CN_BASE_URL, ChatStatus, RoleType } from '@coze/api';

  // 使用个人访问令牌初始化客户端
  const client = new CozeAPI({
    token: 'your_token', // 从 https://www.coze.cn/open/oauth/pats 获取你的 PAT
    // 或者
    // token: async () => {
    //   // 如果令牌过期则刷新
    //   return 'your_oauth_token';
    // },
    baseURL: COZE_CN_BASE_URL,
    allowPersonalAccessTokenInBrowser: true
  });

  // 简单对话示例
  async function quickChat() {
    const v = await client.chat.createAndPoll({
      bot_id: 'your_bot_id',
      additional_messages: [{
        role: RoleType.User,
        content: 'Hello!',
        content_type: 'text',
      }],
    });

    if (v.chat.status === ChatStatus.COMPLETED) {
      for (const item of v.messages ?? []) {
        console.log('[%s]:[%s]:%s', item.role, item.type, item.content);
      }
      console.log('usage', v.chat.usage);
    }
  }
</script>


<style scoped>

</style>
