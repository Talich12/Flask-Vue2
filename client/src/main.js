import Vue from 'vue';
import VueCookies from 'vue-cookies'
import App from './App';
import Vuesax from 'vuesax';
import router from './router';
import VueParticles from 'vue-particles'
import axios from 'axios';

import 'vuesax/dist/vuesax.css';
import 'boxicons/css/boxicons.min.css';
import marked from 'marked';
import _ from 'lodash';
import 'animate.css';

import VueYoutube from 'vue-youtube'

import StoryPage from './components/StoryPage'
import Card from './components/Card';
import Cookie from './components/Cookie'
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import Footer from './components/Footer';
import Information from './components/Information';
import Pagination from './components/Pagination';
import About from './components/About';
import CardRecommendations from './components/CardRecommendations';
import ButtonToTop from './components/ButtonToTop';
import Profile from './components/Profile';
import Notification from './components/Notification';
import MarkdownEditor from './components/MarkdownEditor';
import Subscribers from './components/Subscribers';
import UserComment from './components/UserComment';
Vue.component('usercomment', UserComment)
Vue.component('storypage', StoryPage)
Vue.component('subscriber', Subscribers);
Vue.component('totop', ButtonToTop);
Vue.component('cardrecs', CardRecommendations);
Vue.component('about', About);
Vue.component('pagination', Pagination);
Vue.component('cookie', Cookie);
Vue.component('mdeditor', MarkdownEditor);
Vue.component('logoheader', Header);
Vue.component('sidebar', Sidebar);
Vue.component('card', Card);
Vue.component('myfooter', Footer);
Vue.component('information', Information);
Vue.component('profile', Profile);
Vue.component('notification', Notification);

Vue.use(VueCookies);
Vue.use(VueParticles);
Vue.use(axios)
Vue.use(VueYoutube)

axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response.status === 401) {
      console.log("error")
      const path = 'http://localhost:3000/TokenRefresh'; 
      axios.get(path,{
          headers: {
              'Authorization': 'Bearer ' + window.$cookies.get("refresh_token")
          }
      })
      .then((response) => {
          window.$cookies.set("access_token", response.data.access_token)
          console.log(response.data)
      })
      .catch((error) =>{
        this.$cookies.remove('access_token')
        this.$cookies.remove('refresh_token')
        this.$cookies.remove('login')
        this.$router.push({name: 'Main'})
      })
    }
    else if (error.response.status === 422){
      router.push({name: 'Main'})
    }
    return Promise.reject(error)
  }
)

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  VueCookies,
  router,
  components: { App },
  template: '<App/>',
});
