<template>
   <div class="container">
        <h1>THRIILL TOGETHER</h1>
        <div class="form">
            <h2>Регистрация</h2>
            <div class="title"></div>
            <div class="form_item">
                <h3>Логин</h3>
                <input v-model="Login" type="text">
                <p v-if="data.status === 'Invalid username'">Имя уже занято</p>
            </div>
            <div class="form_item">
                <h3>Пароль</h3>
                <input v-model="Password" type="text">
            </div>
            <div class="form_item">
                <h3>Повторите пароль</h3>
                <input v-model="RepeatPassword" type="text">
                <p v-if="data.status === 'Password not equal'">Пароли не совпадают</p>
            </div>
        </div>
        <button @click="Done()"><h3>Готово</h3></button>
        <p>Еще нет аккаунта?<a href="#/login">Создайте свой аккаунт</a></p>
   </div>
</template>
 
<script>
    import axios from 'axios';
 
    export default {
    name: 'Registration',
    data() {
        return {
        msg: '',
        Login: '',
        Password: '',
        RepeatPassword: '',
        data: [],
        };

    },
    methods: {
        Done() {
        const path = 'http://localhost:8000/registration';
        axios.post(path, {login: this.Login, password: this.Password, repeat_password: this.RepeatPassword})
        .then((response) => {
            console.log(response.data)
            const data = response.data;
            this.data = data;
            if (response.data.status == 'Success'){
                this.$router.push({name: 'Login'})
            }
        })
        .catch((error) =>{
            console.log(error)
        })
        },
        Get(){
        const path = 'http://localhost:8000/registration'; 
        axios.get(path)
        .then((response) => {
            console.log(response.data)
            if (response.data.status == 'Redirect'){
                this.$router.push({name: 'Ping'})
            }
        })
        .catch((error) =>{
            console.log(error)
        })
        },

    },
    created(){
        this.Get();
    },
 
    };
</script>

<style>
    @import '../assets/css/main.css';
    @import '../assets/css/font.css';
</style>