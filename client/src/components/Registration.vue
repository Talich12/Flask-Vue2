<!--<template>


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
        const path = 'http://localhost:3000/registration';
        axios.post(path, { login: this.Login, password: this.Password, repeat_password: this.RepeatPassword })
          .then((response) => {
            console.log(response.data);
            const data = response.data;
            this.data = data;
            console.log(response);
            if (response.data.status == 'Success') {
              this.$router.push({ name: 'Login' });
            }
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
  };
  </script>
  -->
<!--<template>
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


    <vs-button danger transparent :active="active == 1" @click="active = 1">
      Зарегестрируйтесь!
    </vs-button>
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
        <vs-input type="password" v-model="input2" placeholder="Повторите пароль">
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
            Нет аккаунта? <a href="/registration">Создайте новый аккаунт</a>
          </div>
        </div>
      </template>
    </vs-dialog>
  </div>
</template>
<script>

export default {
  data: () => ({
    active: false,
    input1: '',
    input2: '',
    checkbox1: false
  })
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
  margin: 0px;
  margin-top: 20px;
  padding: 0px;
  font-size: 0.7rem;
}

.footer-dialog .new a {
  color: rgba(var(--vs-primary), 1) !important;
  margin-left: 6px;
}

.footer-dialog .new a:hover {
  text-decoration: underline;
}

.footer-dialog .vs-button {
  margin: 0px;
}
</style>
