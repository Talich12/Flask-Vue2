<template>
    <footer class="footer">
      <div class="social-media" style="padding-top: 1%;">
        <p style="margin-bottom: 1%;">Мы в социальных сетях:</p>
        <div class="social-icons">
            <a class="social-icon" href="#"><i class="bx bxl-instagram"></i></a>
            <a class="social-icon" href="#"><i class="bx bxl-telegram"></i></a>
            <a class="social-icon" href="#"><i class="bx bxl-vk"></i></a>
            <a class="social-icon" href="#"><i class="bx bxl-github"></i></a>
        </div>
      </div>
      <form class="newsletter-form">
        <p class="newsletter-text">Подпишитесь на нашу рассылку:</p>
        <input type="email" class="newsletter-input" placeholder="Ваш адрес электронной почты">
        <button class="newsletter-button">Подписаться</button>
      </form>
        <vs-alert :color="color" style="height: 14vh;">
      <template #icon>
        <i class='bx bxs-info-circle' style="font-size: 3vh;"></i>
      </template>
      <template #title>
        <p>
        ThrillTogether
        </p>
      </template>
      <p style="text-align: left; font-size: 2vh;">
      Приветствуем! Сайт разработан тремя студентами ДВФУ обучающимися на направлении Б9121-09.03.03пикд в ходе обучения на втором курсе в рамках дисциплины "Программная инженерия". Больше о сайте можно прочитать во вкладке "О нас". Вся необходимая информация дана ниже.
      </p>
    </vs-alert>
      <p class="description" style="color: rgb(238, 239, 249); margin-top: 1%;">
        Пугаем вас уже вот столько дней: {{ randomNumber }} 
      </p>
      <div class="footer-links">
        <div class="footer-column">
          <h5 class="footer-heading">Оказать помощь ресурсу</h5>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">Криптовалюта</a></li>
            <li><a href="#" class="footer-link">Перевод</a></li>
            <li><a href="#" class="footer-link">Boosty</a></li>
            <li><a href="#" class="footer-link">Предложить идею</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h5 class="footer-heading">Контактная информация</h5>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">VKontakte</a></li>
            <li><a href="#" class="footer-link">Telegram</a></li>
            <li><a href="#" class="footer-link">Instagram</a></li>
            <li><a href="#" class="footer-link">Mail</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h5 class="footer-heading">Для разработчиков</h5>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">Наша команда</a></li>
            <li><a href="#" class="footer-link">Работать с нами</a></li>
            <li><a href="#" class="footer-link">Сообщить об ошибке</a></li>
            <li><a href="#" class="footer-link">Github</a></li>
        </ul>
</div>
<div class="footer-column">
  <h5 class="footer-heading">Часто задаваемые вопросы</h5>
  <ul class="footer-list">
    <li><a href="#" class="footer-link">О нас</a></li>
    <li><a href="#" class="footer-link">Как стать автором?</a></li>
    <li><a href="#" class="footer-link">Интро сайта</a></li>
    <li><a href="#" class="footer-link">Удалить аккаунт</a></li>
  </ul>
</div>
</div>
<p class="footer-text">
  © 2023 Copyright:
  <a class="text-white" style="color: rgb(106, 78, 147)" href="https://thrilltogether.ru/">ThrillTogether.ru</a> <a>Все права защищены</a>
</p>
</footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      randomNumber: 0,
      color: 'danger'
    };
  },
  mounted() {
    this.randomNumber = Math.floor(Math.random() * 100);
  },
};
</script>

<style>
.footer {
  z-index: 20;
  background-color: #25252f;
  margin-top: 2%;
  margin-left: 16%;
  color: white;
  text-align: center;
}

li {
    font-size: small;
    margin-top: 10px;
}

h5 {
    font-weight: bolder;
}

.social-media {
  margin-bottom: 20px;
}

.social-icon {
  color: white;
  font-size: 24px;
  margin: 0 5px;
}

.newsletter-form {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.newsletter-text {
  margin-right: 10px;
}

.newsletter-input {
  padding: 8px;
  border: none;
  border-radius: 5px;
  font-size: 1vw;
  color:#ffffff;
  width: 20vw;
  background-color: rgb(62, 62, 74);
}

.newsletter-button {
  padding: 8px 20px;
  border: none;
  font-size: 1vw;
  border-radius: 5px;
  background-color: rgb(48, 48, 58);
  color: #ffffff;
}

.description {
  color: rgb(188, 188, 188);
  font-weight:lighter;
  font-size: small;
  margin-bottom: 20px;
}

.footer-links {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.footer-column {
  margin: 0 20px;
}

.footer-heading {
  margin-bottom: 10px;
}

.footer-list {
  list-style-type: none;
  padding: 0;
}

.footer-link {
  color: rgb(188, 188, 188);
  text-decoration: none;
  margin-bottom: 5px;
}

.footer-text {
  background-color: rgba(0, 0, 0, 0.2);
  padding: 10px;
}
</style>  