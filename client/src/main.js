import Vue from 'vue';
import VueCookies from 'vue-cookies'
import App from './App';
import Vuesax from 'vuesax';
import router from './router';

import 'vuesax/dist/vuesax.css';
import 'boxicons/css/boxicons.min.css';

import Card from './components/Card';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import Footer from './components/Footer';
import Information from './components/Information';
Vue.component('logoheader', Header);
Vue.component('sidebar', Sidebar);
Vue.component('card', Card);
Vue.component('myfooter', Footer);
Vue.component('information', Information);

Vue.use(VueCookies);

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  VueCookies,
  router,
  components: { App },
  template: '<App/>',
});