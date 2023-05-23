import Vue from 'vue';
import Vuesax from 'vuesax';
import Router from 'vue-router';
import Registration from '@/components/Registration';
import Login from '@/components/Login';
import Index from '@/components/Index';
import Main from '@/components/Main';
import StoryAdd from '@/components/StoryAdd';
import About from '@/components/About';
import Profile from '@/components/Profile';

import 'vuesax/dist/vuesax.css';
import 'boxicons';

Vue.use(Router);
Vue.use(Vuesax, {
  colors: {
    primary:'rgb(42, 42, 53)',
    dark:'rgb(48, 48, 58)',
    success:'rgb(238, 239, 249)',
    danger:'rgb(106, 78, 147)',
  }
})
 
export default new Router({
  mode: "hash",
  routes: [
    {
      path: '/storyadd',
      name: 'StoryAdd',
      component: StoryAdd
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
      path: '/',
      name: 'Main',
      component: Main,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
    {
      path: '/profile/:username',
      name: 'Profile',
      component: Profile,
    },
  ],
});