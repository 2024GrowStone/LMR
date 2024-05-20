<!-- Login.vue -->
<template>
    <main class="main_container">
        <div class="login_container">
            <div>
                <img class="school_icon" src="../assets/icons/inha_logo.jpg" alt="school logo">
            </div>
            <form class="login_box">
                <div>
                    <input class="id_input" type="text" id="username" name="username" placeholder="인하대학교 아이디">
                </div>
                <div>
                    <input class="pw_input" type="password" id="password" name="password" placeholder="인하대학교 비밀번호">
                </div>
                <div>
                    <button class="login_btn" type="submit">로그인</button>
                </div>
            </form>
        </div>
    </main>
</template>

<style src="../assets/Login.css" scoped>
</style>