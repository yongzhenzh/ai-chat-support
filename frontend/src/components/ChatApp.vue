
        const response = await fetch("http://localhost:8000/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            user_id: this.userId,
            query: this.query,
            history: this.chatHistory,
          }),
        });

        const data = await response.json();
<template>
  <div class="layout">
    <!-- Left: Chat Interface -->
    <div class="chat-panel">
      <div class="user-selector">
        <label for="user">User:</label>
        <select id="user" v-model="userId" @change="switchUser">
          <option v-for="id in userIds" :key="id" :value="id">{{ id }}</option>
        </select>
      </div>

      <div class="chat-container">
        <div class="messages" ref="messages">
          <div v-for="(msg, index) in chatHistory" :key="index" class="message">
            <strong>{{ msg.role }}:</strong> {{ msg.content }}
          </div>
          <div v-if="loading" class="loading">Loading...</div>
        </div>

        <div class="input-container">
          <input v-model="query" @keyup.enter="sendMessage" placeholder="Type your message..." :disabled="loading" />
          <button @click="sendMessage" :disabled="loading || !query.trim()">Send</button>
        </div>
      </div>
    </div>

    <!-- Right: Info Panel -->
    <div class="info-panel">
      <h2>Medical AI Chat Support</h2>
      <p>Powered by Retrieval-Augmented Generation (RAG)</p>

      <h3>Available Users</h3>
      <ul>
        <li>u001: Diabetes + Metformin</li>
        <li>u002: Post Heart Surgery</li>
        <li>u003: Hypertension + Lisinopril</li>
        <li>u004: New user (no history)</li>
        <li>u005: Allergic to penicillin/sulfa</li>
        <li>u006: Elderly with chronic conditions</li>
        <li>u007: Child with asthma</li>
        <li>u008: Pregnant</li>
      </ul>

      <h3>Medical Knowledge Base</h3>
      <ul>
        <li>depression</li>
        <li>diabetes</li>
        <li>heart disease</li>
        <li>migraine</li>
        <li>schizophrenia</li>
        <li>vitamin B12 deficiency</li>
      </ul>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      userId: "u001",
      userIds: ["u001", "u002", "u003", "u004", "u005", "u006", "u007", "u008"],
      query: "",
      loading: false,
      chatHistory: [],
    };
  },
  mounted() {
    this.loadChat();
  },
  methods: {
    loadChat() {
      const stored = localStorage.getItem(`chatHistory_${this.userId}`);
      this.chatHistory = stored ? JSON.parse(stored) : [];
    },
    switchUser() {
      this.query = "";
      this.loadChat();
    },
    async sendMessage() {
      if (!this.query.trim()) return;

      this.chatHistory.push({ role: "user", content: this.query });
      this.loading = true;

      try {
        const response = await fetch("http://localhost:8000/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            user_id: this.userId,
            query: this.query,
            history: this.chatHistory,
          }),
        });
        const data = await response.json();
        this.chatHistory.push({ role: "assistant", content: data.answer });
        localStorage.setItem(`chatHistory_${this.userId}`, JSON.stringify(this.chatHistory));
      } catch (error) {
        this.chatHistory.push({ role: "assistant", content: "Error: Failed to fetch response." });
      } finally {
        this.query = "";
        this.loading = false;
        this.$nextTick(() => {
          const el = this.$refs.messages;
          el.scrollTop = el.scrollHeight;
        });
      }
    },
  },
};
</script>

<style scoped>
.layout {
  display: flex;
  height: 100vh;
  width: 100vw;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.chat-panel {
  width: 50vw; 
  padding: 20px;
  border-right: 1px solid #ddd;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.user-selector {
  margin-bottom: 10px;
}

.chat-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  padding: 16px;
  border-radius: 8px;
  background: #fff;
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 10px;
  white-space: pre-wrap;
  word-wrap: break-word;
}

.message {
  margin: 5px 0;
}

.loading {
  font-style: italic;
  color: gray;
}

.input-container {
  display: flex;
  gap: 8px;
}

input {
  flex: 1;
  padding: 8px;
  font-size: 16px;
}

button {
  padding: 8px 16px;
  font-size: 16px;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.info-panel {
  width: 50vw;
  padding: 20px;
  background: #f5f5f5;
  overflow-y: auto;
  text-align: left;
}

.info-panel h2 {
  font-size: 22px;
  margin-bottom: 8px;
}

.info-panel h3 {
  margin-top: 20px;
  margin-bottom: 8px;
}

.info-panel ul {
  list-style-type: disc;
  margin-left: 20px;
}

.info-panel li {
  margin-bottom: 6px;
}
</style>
