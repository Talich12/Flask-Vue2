<template>
    <div class="notification-cotainer">
        <div class="notification-header">
            <span class="notification-username">Уведомления</span>
            <div class="notification-settings">
                <Settings>
                </Settings>
            </div>
        </div>
        <div class="notification-alert">
            <template>
                <vs-alert shadow :hidden-content.sync="hidden" color="rgb(106, 78, 147)">
                    <template #title style="color: rgb(238, 239, 249);">
                        Подписки
                    </template>
                    У вас новый подписчик!
                </vs-alert>
            </template>
        </div>
    </div>
</template>



<script>


import Settings from './Settings.vue'

export default {
    components: {
        Settings
    },
    data: () => ({
        active: false,
        hidden: true
    })
}
</script>

<style>
.notification-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding-left: 16%;
    padding-top: 6%;
}

.notification-username {
    padding-left: 2%;
    font-size: 2vw;
    color: rgb(238, 239, 249);
}

.notification-text {
    font-size: 2.5vw;
    color: rgb(238, 239, 249);

}

.notification-alert {
    display: flex;
    justify-content: space-between;
    margin-left: 16%;
    margin-top: 2%;
    color: rgb(238, 239, 249);
}
</style>