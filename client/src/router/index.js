import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Registration from '@/components/Registration';
 
Vue.use(Router);
 
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/Regist',
      name: 'Registration',
      component: Registration,
    },
  ],
});