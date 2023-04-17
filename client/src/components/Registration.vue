<template>
    <div>
        <input v-model="Login" type="text" placeholder="Login">
        <input v-model="Password" type="text" placeholder="Password">
        <input v-model="RepeatPassword" type="text" placeholder="Repeat password">
        <p v-if="this.data.status === 'Password not equal'">Пароли не совпадают</p>
        <p v-if="this.data.status === 'Invalid username'">Данный логин уже занят</p>
        <button @click="Done()">Done</button>
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
        const path = 'http://localhost:8000/Registration';
        axios.post(path, {login: this.Login, password: this.Password, repeat_password: this.RepeatPassword})
        .then((response) => {
            console.log(response.data)
            const data = response.data;
            this.data = data;
            if (response.data.status == 'Success'){
                this.$router.push({name: 'Ping'})
            }
        })
        .catch((error) =>{
            console.log(error)
        })
        },
        Get(){
        const path = 'http://localhost:8000/Registration'; 
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