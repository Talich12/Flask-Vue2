import Vue from 'vue';
import Router from 'vue-router';
import Registration from '@/components/Registration';
import Login from '@/components/Login';
import Index from '@/components/Index';
import Main from '@/components/MainPage';
 
Vue.use(Router);
 
export default new Router({
  mode: "hash",
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/main',
      name: 'Main',
      component: Main,
    },
  ],
});