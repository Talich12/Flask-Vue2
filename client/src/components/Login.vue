<!--
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
                this.$cookies.set("login", this.Login)
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
-->
<template>
    <div class="center">

        <button @click="active = !active"
            style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder; border: none; background-color: transparent; cursor: pointer; color: rgb(255, 255, 255)">
            Вход
        </button>
        <vs-dialog blur v-model="active">
            <template #header>
                <h4 class="not-margin">
                    <b>Thrill Together</b>
                </h4>
            </template>


            <div class="con-form">
                <vs-input v-model="input1" placeholder="Email">
                    <template #icon>
                        @
                    </template>
                </vs-input>
                <vs-input type="password" v-model="input2" placeholder="Пароль">
                    <template #icon>
                        <i class='bx bxs-lock'></i>
                    </template>
                </vs-input>
                <div class="flex">
                    <vs-checkbox v-model="checkbox1">Запомнить меня</vs-checkbox>
                    <a href="#">Забыли пароль?</a>
                </div>
            </div>

            <template #footer>
                <div class="footer-dialog">
                    <vs-button block>
                        Войти
                    </vs-button>
                    <div class="new">
                        <p>Нет аккаунта?</p> <Registration></Registration>
                    </div>
                </div>
            </template>
        </vs-dialog>
    </div>
</template>
<script>
import Registration from './Registration.vue'
export default {
    data: () => ({
        active: false,
        input1: '',
        input2: '',
        checkbox1: false
    }),
    components: {
        Registration
    }
}
</script>
<style>
.not-margin {
    margin: 0px;
    font-weight: normal;
    padding: 10px;
}

.con-form {
    width: 100%;
    margin-bottom: 6%;
}

.con-form .flex {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.con-form .flex a {
    font-size: 0.8rem;
    opacity: 0.7;
}

.con-form .flex a:hover {
    opacity: 1;
}

.con-form .vs-checkbox-label {
    font-size: 0.8rem;
}

.con-form .vs-input-content {
    margin: 10px 0px;
    width: calc(100%);
}

.con-form .vs-input {
    width: 100%;
}

.footer-dialog {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    width: calc(100%);
}

.footer-dialog .new {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
    font-size: 0.7rem;
    
}


.footer-dialog .new a:hover {
    text-decoration: underline;
}

.footer-dialog .vs-button {
    margin: 0px;
}
</style>
