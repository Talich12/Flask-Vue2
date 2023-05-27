<template>
    <div class="profile">
        <div class="profile-header__content">
            <div class="profile__user">
                <div class="profile__user-avatar">
                    <vs-avatar :loading = "loading" size="70" class="avatar">
                        <img :src="UserIcon" alt="">
                    </vs-avatar>
                </div>
                <div class="profile__user-name">
                    <span class="username">{{ $route.params.username }}</span>
                </div>
                <div class="profile-rank-cog">
                    <div class="profile__user-rank">
                        <vs-button danger size="large" shadow :active="active == 0" @click="active = 0" class="rank">
                            Рейтинг
                        </vs-button>
                    </div>
                    <div v-if="User.access == true"   class="profile__user-rank">
                        <vs-button danger size="large" shadow :active="active == 0" @click="active = 0" class="rank">
                            Подписаться
                        </vs-button>
                    </div>
                    <div v-if="User.access == true"  class="profile__cog">
                        <vs-button icon color="danger" shadow :active="active == 0" @click="active = 0" class="cog">
                            <i class='bx bxs-cog'></i>
                        </vs-button>
                    </div>
                </div>

            </div>
            <div v-if="User.access == true"  class="profile__writer">
                <vs-button danger size="large" shadow upload to="/storyadd" class="write-history">
                    Написать Историю
                </vs-button>
            </div>
        </div>
        <div class="profile__navbar">
            <div class="center examplex">
                    <vs-navbar dark text-white square left-collapsed v-model="active">
                        
                        <vs-navbar-item @click="Get" :active="active == 'post'" id="post" style="font-size: 1vw;"> Мои истории </vs-navbar-item>
                        <vs-navbar-item @click="GetFollowers()" :active="active == 'subscribers'" id="subscribers" style="font-size: 1vw;"> Подписчики </vs-navbar-item>
                        <vs-navbar-item @click="GetFollowed()" :active="active == 'subscription'" id="subscription" style="font-size: 1vw;"> Подписки </vs-navbar-item>
                        <vs-navbar-item :active="active == 'achievements'" id="achievements" style="font-size: 1vw;"> Достижения </vs-navbar-item>
                        
                    </vs-navbar>
                    <div class="square animate__animated animate__fadeIn" style="animation-duration: 1s; width: 84%;">
                        <div v-if="active == 'post'">
                            <div class="containerProfile">
                            <vs-row justify="space-around" style="margin-top: 6%;">
                                <vs-col v-for="post in Data" offset="1" w="5">
                                <card>
                                    <template #title>
                                    {{ post.title }}
                                    </template>
                                    <template #text>
                                    {{ post.body }}
                                    </template>
                                    <template #img>
                                    <img :src="require(`@/assets/img/load/${post.img}`)" alt="">
                                    </template>
                                </card>
                                </vs-col>
                            </vs-row>
                            </div>
                        </div>
                        <div v-if="active == 'subscribers'">
                            <div class="containerSubscribers">
                                <subscriber :users="Users"></subscriber>
                            </div>
                        </div>
                        <div v-if="active == 'subscription'">
                            <div class="containerSubscribers">
                                <subscriber @path="onRoute" :users="Users"></subscriber>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
    </div>
</template>
  

<script>
import axios from 'axios';

export default {
    data() {
        return {
            loading: false,
            active: 'post',
            Data: [],
            User: [],
            UserIcon: require(`@/assets/img/load/sample1.jpg`),
            Users: [],
        };
    },
    methods: {
        Get() {
            const path = "http://localhost:3000"+this.$route.path+ "/posts";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                const data = response.data;
                this.Data = data;
            })
                .catch((error) => {
                console.log(error);
            });
        },
        GetFollowers(){
            const path = "http://localhost:3000"+this.$route.path+"/followers";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                const data = response.data;
                this.Users = data;
            })
                .catch((error) => {
                console.log(error);
            });
        },
        GetFollowed(){
            const path = "http://localhost:3000"+this.$route.path+"/followed";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                const data = response.data;
                this.Users = data;
            })
                .catch((error) => {
                console.log(error);
            });
        },
        GetUserData(){
            const path = "http://localhost:3000"+this.$route.path;
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                const data = response.data;
                this.User = data;
                this.UserIcon = require(`@/assets/img/load/${data.avatar}`)
            })
                .catch((error) => {
                console.log(error);
            });
        },
        onRoute(data){
            console.log(data)
        }
    },
    watch:{
        '$route' (to, from){
            this.loading = true
            this.active = "post"
            this.Get();
            this.GetUserData();
            this.loading = false
        }
    },
    created() {
        this.loading = true
        this.Get();
        this.GetUserData();
        this.loading = false
    },
}
</script>

<style>
.profile-header__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(48, 48, 58);
    padding: 1%;
    padding-top: 6%;
}
.profile {
    overflow-x: hidden;
}

.profile__user {
    display: flex;
    align-items: center;
    padding-left: 22%;
}

.profile__user-name {
    margin-left: 2%;
}

.username {
    font-size: 2vw;
    color: rgb(238, 239, 249);
}

.profile__writer {
    display: flex;
    align-items: center;
    margin-right: 6%;
}

.profile-rank-cog {
    display: flex;
    align-items: center;
}

.rank, .cog {
    margin-left: 0.5vw;
}
.profile__navbar{
    position: relative;
    z-index: 1;
}
.vs-navbar-content{
    margin-left: 7%;
}
.center{
    display: flex;
    justify-content: center;
}
.containerProfile {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Высота экрана, чтобы футер всегда был внизу */
  margin-left: 16%;
  margin-right: 7%;
}
.containerSubscribers {
  width: 89%;
  padding-top: 6%;
  padding-left: 15%;
}

</style>
  