import Vue from 'vue';
import VueCookies from 'vue-cookies'
import App from './App';
import router from './router';

Vue.use(VueCookies);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  VueCookies,
  router,
  components: { App },
  template: '<App/>',
});
