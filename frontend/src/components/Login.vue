<!-- Login.vue -->
<template>
    <main class="main_container">
        <div class="login_container">
            <div>
                <img class="school_icon" src="../assets/icons/inha_logo.jpg" alt="school logo">
            </div>
            <form class="login_box" @submit.prevent="submitForm">
                <div>
                    <input class="id_input medium" type="text" id="username" v-model="username" placeholder="인하대학교 아이디" required>
                </div>
                <div>
                    <input class="pw_input medium" type="password" id="password" v-model="password" placeholder="인하대학교 비밀번호" required>
                </div>
                <div>
                    <button class="login_btn medium" type="submit">로그인</button>
                </div>
            </form>
        </div>
    </main>
</template>

<style src="../assets/Login.css" scoped>
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      response: null,
      error: null
    };
  },
  methods: {
    async submitForm() {
      this.response = null;
      this.error = null;
      try {
        // login successed
        const res = await axios.post('http://localhost:8000/login', {
          username: this.username,
          password: this.password
        });
        this.response = res.data;
        alert("로그인에 성공하였습니다.")
      } catch (error) {
        // login failed
        alert("로그인에 실패하였습니다.");

        this.error = error.response.data.detail || 'An error occurred';
      }
    }
  }
};
</script>
