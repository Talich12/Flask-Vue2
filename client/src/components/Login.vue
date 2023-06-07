<template>
    <div class="center">

        <button id="logbtn" @click="active = !active"
            style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder; border: none; background-color: transparent; cursor: pointer; color: rgb(255, 255, 255)">
            <vs-button
        gradient
        style="min-width: 44px; min-height: 44px; margin: 0;"
        danger
        animation-type="scale"
      >
      <i class='bx bx-log-in'></i>
        <template #animate >
          Вход
        </template>
      </vs-button>
        </button>
        <vs-dialog blur v-model="active">
            <template #header>
                <h4 class="not-margin">
                    <b>Thrill Together</b>
                </h4>
            </template>


            <div class="con-form">
                <vs-input  danger border v-model="Login" placeholder="Логин">
                    <template #icon>
                        <i class='bx bxs-user'></i>
                    </template>
                </vs-input>
                <vs-input danger border type="password" v-model="Password" placeholder="Пароль">
                    <template v-if="error" #message-danger >
                        Неправильно введён логин или пароль
                    </template>
                    <template #icon>
                        <i class='bx bxs-lock'></i>
                    </template>
                </vs-input>
            </div>

            <template #footer>
                <div class="footer-dialog">
                    <vs-button @click="Done()" block>
                        Войти
                    </vs-button>
                    <div class="new">
                        <p>Нет аккаунта?</p>
                        <Registration></Registration>
                    </div>
                </div>
            </template>
        </vs-dialog>
    </div>
</template>
<script>
import Registration from './Registration.vue'
import axios from 'axios';
export default {
    data: () => ({
        active: false,
        Login: '',
        Password: '',
        error: false,
    }),
    methods: {
        Done() {
            const path = 'http://localhost:3000/login';
            axios.post(path, { login: this.Login, password: this.Password })
            .then((response) => {
                console.log(response.data)
                const data = response.data;
                this.data = data;
                this.$cookies.set("access_token", data.access_token)
                this.$cookies.set("refresh_token", data.refresh_token)
                this.$cookies.set("login", this.Login)
                console.log($cookies.get('login'))
                console.log(response)
                if (response.data.status == 'Success') {
                    this.active = false
                }
                else {
                    this.error = true
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },
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

#logbtn {
    padding: 0;
}

.footer-dialog .new a:hover {
    text-decoration: underline;
}

.footer-dialog .vs-button {
    margin: 0px;
}
</style>
