<template>
  <div class="containerInfoAbout animate__animated animate__fadeIn" style="animation-duration: 1s; justify-content: center; align-items: center;">
    <vs-row justify="space-around">
      <vs-alert shadow color="success" style="margin-left: 8%; z-index: 0;">
        <template #title>
          О сайте ThrillTogether
        </template>
        Информацию о разработчиках можно получить внизу страницы. На этой вкладке будет описано как пользоваться различным функционалом сайта и какую информацию можно получить из различных элементов. Запустите ознакомление ниже.
      </vs-alert>
      <vs-button
        size="xl"
        success
        border
        style="margin-top: 6vh; margin-left: 7%;"
        @click="openNotifications"
      >
        <i class='bx bx-message-square-detail' style="margin-right: 0.5vw;"></i> Запустить ознакомительную часть
      </vs-button>
    </vs-row>
    <vue-particles
      color="#6A4E93"
      :particleOpacity="0.4"
      :particlesNumber="50"
      shapeType="circle"
      :particleSize="4"
      linesColor="#6A4E93"
      :linesWidth="1.2"
      :lineLinked="true"
      :lineOpacity="0.5"
      :linesDistance="180"
      :moveSpeed="1.5"
      :hoverEffect="false"
      hoverMode="grab"
      :clickEffect="false"
      clickMode="push"
      style="position:absolute; z-index: -10; height: 100%; width: 100vw; left: 0%; top: 8%;"
    ></vue-particles>
  </div>
</template>

<script>
export default {
  methods: {
    openNotifications() {
      const icons = [
        "<i class='bx bx-bell'></i>",
        "<i class='bx bx-pen'></i>",
        "<i class='bx bx-edit'></i>",
        "<i class='bx bx-medal'></i>"
      ];

      const positions = [
        "bottom-right",
        "top-right",
        "top-center",
        "top-left"
      ];

      const titles = ["Начало работы", "Истории", "Публикация", "Достижения"];

      const texts = [
        "Для того, чтобы использовать всю функциональность нашего сайта, вам необходимо зарегистрироваться. Сделать это вы можете, нажав на кнопку \"Войти\" в нижнем левом углу.\nПосле регистрации у вас создастся личный кабинет, в котором вы сможете посмотреть свой рейтинг, подписки и подписчиков, а также ваши истории.",
        "На главной странице нашего сайта вы можете просматривать самые популярные истории. В левом меню доступны различные фильтры историй, а также отдельный поиск. Вы можете сохранять и комментировать истории, а также подписываться на их авторов.",
        "Вы можете сами стать писателем страшных историй! Для этого в личном кабинете нажмите кнопку \"Написать историю\". Перед вами откроется редактор, в котором вы можете добавить сам текст истории, изображения к ней, видео и аудио. Когда вы завершите написание истории, нажмите \"Моя история готова\". Так вы опубликуете свою историю!",
        "Являясь пользователем нашего сайта, вы можете получать различные достижения. Мы уверены, что система достижений будет мотивировать вас и других пользователей читать и писать страшные истории."
      ];

      let delay = 0;
      for (let i = 0; i < icons.length; i++) {
        setTimeout(() => {
          const noti = this.$vs.notification({
            icon: icons[i],
            duration: 20000,
            color: "dark",
            width: "500px",
            border: "danger",
            progress: 'auto',
            position: positions[i % positions.length],
            title: titles[i],
            text: texts[i],
            classes: "pulsating-notification"
          });
        }, delay);
        delay += 20000;
      }
    }
  }
};
</script>

<style>
.containerInfoAbout {
  display: flex;
  flex-direction: column;
  min-height: 40vh;
  padding-left: 16%;
  padding-right: 7%;
  padding-top: 8%;
}

.vs-notification {
  /*animation: pulsate 1.5s infinite;*/
}

@keyframes pulsate {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
</style>