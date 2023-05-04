import Vue from 'vue';
import VueCookies from 'vue-cookies'
import App from './App';
import router from './router';
import Vuesax from 'vuesax';

Vue.use(VueCookies);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  VueCookies,
  router,
  Vuesax,
  components: { App },
  template: '<App/>',
});
