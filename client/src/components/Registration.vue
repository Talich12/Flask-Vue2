<template>
  <div class="center">
    <vs-button danger transparent :active="active == true" @click="active = true">
      Зарегистрируйтесь!
    </vs-button>
    <vs-dialog blur v-model="active">
      <template #header>
        <h4 class="not-margin">
          <b>Thrill Together</b>
        </h4>
      </template>

      <div class="con-form">
        <vs-input danger border v-model="Login" placeholder="Логин">
          <template v-if="error1" #message-danger>
            Данный логин уже занят
          </template>
          <template #icon>
            <i class="bx bxs-user"></i>
          </template>
        </vs-input>
        <vs-input danger border type="password" v-model="Password" placeholder="Пароль">
          <template #message-danger>
            <span v-if="!isPasswordValid">Пароль должен быть длиннее 8 символов и содержать специальные символы</span>
          </template>
          <template #icon>
            <i class="bx bxs-lock"></i>
          </template>
        </vs-input>
        <vs-input danger border type="password" v-model="RepeatPassword" placeholder="Повторите пароль">
          <template v-if="error2" #message-danger>
            Пароли не совпадают
          </template>
          <template #icon>
            <i class="bx bxs-lock"></i>
          </template>
        </vs-input>
      </div>

      <template #footer>
        <div class="footer-dialog">
          <vs-button @click="Done()" block relief danger>
            Зарегистрироваться
          </vs-button>
        </div>
      </template>
    </vs-dialog>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      active: false,
      Login: '',
      Password: '',
      RepeatPassword: '',
      data: [],
      error1: false,
      error2: false,
    };
  },
  computed: {
    isPasswordValid() {
      const regex = /^(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;
      return regex.test(this.Password);
    },
  },
  methods: {
    Done() {
      const path = 'http://localhost:3000/registration';
      if (!this.error2 && this.isPasswordValid) {
        axios
          .post(path, { login: this.Login, password: this.Password })
          .then((response) => {
            console.log(response.data);
            const data = response.data;
            this.data = data;
            console.log(response);
            if (response.data.status == 'Success') {
              this.active = false;
            } else {
              this.error1 = true;
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  watch: {
    RepeatPassword() {
      if (this.Password !== this.RepeatPassword) {
        this.error2 = true;
      } else {
        this.error2 = false;
      }
    },
  },
};
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