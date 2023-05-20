<template>
    <div class="profile">
        <div class="profile-header__content">
            <div class="profile__user">
                <div class="profile__user-avatar">
                    
                    <vs-avatar  size="70" class="avatar">
                        <img src="../assets/img/load/sample1.jpg" alt="">
                    </vs-avatar>
                </div>
                <div class="profile__user-name">
                    <span class="username">Имя пользователя</span>
                </div>
                <div class="profile-rank-cog">
                    <div class="profile__user-rank">
                        <vs-button danger size="large" flat:active="active == 0" @click="active = 0" class="rank">
                            Рейтинг
                        </vs-button>
                    </div>
                    <div class="profile__cog">
                        <vs-button icon color="danger" flat:active="active == 0" @click="active = 0" class="cog">
                            <i class='bx bxs-cog'></i>
                        </vs-button>
                    </div>
                </div>

            </div>
            <div class="profile__writer">
                <vs-button danger size="large" flat:active="active == 0" @click="active = 0" class="write-history">
                    Написать Историю
                </vs-button>
            </div>
        </div>
        <div class="profile__navbar">
            <template>
                <div class="center examplex">
                    <vs-navbar dark text-white square left-collapsed v-model="active">
                        
                        <vs-navbar-item :active="active == 'post'" id="post" style="font-size: 1vw;"> Мои истории </vs-navbar-item>
                        <vs-navbar-item :active="active == 'subscribers'" id="subscribers" style="font-size: 1vw;"> Подписчики </vs-navbar-item>
                        <vs-navbar-item :active="active == 'subscription'" id="subscription" style="font-size: 1vw;"> Подписки </vs-navbar-item>
                        <vs-navbar-item :active="active == 'achievements'" id="achievements" style="font-size: 1vw;"> Достижения </vs-navbar-item>
                        
                    </vs-navbar>
                    <div class="square">
                        <div class="child"> child 1 </div>
                        <div class="child"> child 2 </div>
                        <div class="child"> child 3 </div>
                    </div>
                </div>
            </template>
        </div>
    </div>
</template>
  
<script>
export default {
    data: () => ({
        active: 0
    })
}

</script>
  <script>
  export default {
    data:() => ({
      active: 'guide'
    })
  }
  </script>

<style>
.profile-header__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(48, 48, 58);
    padding: 20px;
}

.profile__user {
    display: flex;
    align-items: center;
    padding-left: 240px;
    padding-top: 60px;
}

.profile__user-name {
    margin-left: 20px;
}

.username {
    font-size: 24px;
    color: rgb(238, 239, 249);
}

.profile__writer {
    display: flex;
    align-items: center;
    padding-top: 60px;
}

.profile-rank-cog {
    display: flex;
    align-items: center;
}

.rank,
.cog {
    margin-left: 20px;
}
.profile__navbar{
    position: relative;
    z-index: 1;
}
.center{
    display: flex;
    justify-content: center;
}

</style>
  