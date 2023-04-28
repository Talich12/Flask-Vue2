<template>
    <div class="container">
         <h1>THRIILL TOGETHER</h1>
         <div class="form">
             <h2>Войти</h2>
             <div class="title"></div>
             <div class="form_item">
                 <h3>Логин</h3>
                 <input v-model="Login" type="text">
             </div>
             <div class="form_item">
                 <h3>Пароль</h3>
                 <input v-model="Password" type="text">
             </div>
         </div>
         <p v-if="data.status === 'Invalid username' ">Не правильный логин или пароль</p>
         <button @click="Done()"><h3>Готово!</h3></button>
         <p>Еще нет аккаунта?<a href="#/registration">Создайте свой аккаунт</a></p>
    </div>
 </template>
  
 <script>
     import axios from 'axios';
  
     export default {
     name: 'Login',
     data() {
         return {
         Login: '',
         Password: '',
         data: [],
         };
 
     },
     methods: {
         Done() {
         const path = 'http://localhost:3000/login';
         axios.post(path, {login: this.Login, password: this.Password})
         .then((response) => {
             console.log(response.data)
             const data = response.data;
             this.data = data;
             this.$cookies.set("access_token", data.access_token)
             this.$cookies.set("refresh_token", data.refresh_token)
             console.log(response)
             if (response.data.status == 'Success'){
                this.$router.push({name: 'Index'})
             }
         })
         .catch((error) =>{
             console.log(error)
         })
         },

 
     },
  
     };
 </script>
 
 <style>
     @import '../assets/css/main.css';
     @import '../assets/css/font.css';
 </style>