<template>

</template>

<script>
import AcceptCookie from './AcceptCookie.vue'
    export default {
    data() {
      return {
        active: false
      };
    },
    created() {
        this.openNotification();
    },
    methods: {
    openNotification() {
        this.$vs.notification({
        title: 'Cookie',
        text: `Для корректной работы нашего сайта необходимо использование cookie-файлов`,
        icon: `<i class='bx bx-cookie' ></i>`,
        color: 'danger',
        progress: 'auto',
        flat: 'true',
        duration: '20000',
        content: AcceptCookie,
        clickClose: true
        })
    }
    }
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Unbounded&display=swap');
</style>