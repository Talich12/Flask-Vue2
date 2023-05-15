<template>
    <footer class="footer">
      <div class="social-media">
        <a class="social-icon" href="#"><i class="bx bxl-facebook"></i></a>
        <a class="social-icon" href="#"><i class="bx bxl-twitter"></i></a>
        <a class="social-icon" href="#"><i class="bx bxl-google"></i></a>
        <a class="social-icon" href="#"><i class="bx bxl-instagram"></i></a>
        <a class="social-icon" href="#"><i class="bx bxl-linkedin"></i></a>
        <a class="social-icon" href="#"><i class="bx bxl-github"></i></a>
      </div>
      <form class="newsletter-form">
        <p class="newsletter-text">Подпишитесь на нашу рассылку:</p>
        <input type="email" class="newsletter-input" placeholder="Email address">
        <button class="newsletter-button">Subscribe</button>
      </form>
      <p class="description">
        Сайт разработан тремя студентами ДВФУ обучающимися на направлении Б9121-09.03.03пикд. Вся необходимая информация дана ниже.
      </p>
      <p class="description" style="color: rgb(106, 78, 147)">
        Пугаем вас уже вот столько дней: {{ randomNumber }} 
      </p>
      <div class="footer-links">
        <div class="footer-column">
          <h5 class="footer-heading">Links</h5>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">Link 1</a></li>
            <li><a href="#" class="footer-link">Link 2</a></li>
            <li><a href="#" class="footer-link">Link 3</a></li>
            <li><a href="#" class="footer-link">Link 4</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h5 class="footer-heading">Links</h5>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">Link 1</a></li>
            <li><a href="#" class="footer-link">Link 2</a></li>
            <li><a href="#" class="footer-link">Link 3</a></li>
            <li><a href="#" class="footer-link">Link 4</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h5 class="footer-heading">Links</h5>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">Link 1</a></li>
            <li><a href="#" class="footer-link">Link 2</a></li>
            <li><a href="#" class="footer-link">Link 3</a></li>
            <li><a href="#" class="footer-link">Link 4</a></li>
        </ul>
</div>
<div class="footer-column">
  <h5 class="footer-heading">Links</h5>
  <ul class="footer-list">
    <li><a href="#" class="footer-link">Link 1</a></li>
    <li><a href="#" class="footer-link">Link 2</a></li>
    <li><a href="#" class="footer-link">Link 3</a></li>
    <li><a href="#" class="footer-link">Link 4</a></li>
  </ul>
</div>
</div>
<p class="footer-text">
  © 2023 Copyright:
  <a class="text-white" style="color: rgb(106, 78, 147)" href="https://thrilltogether.ru/">ThrillTogether.ru</a> <a>все права соблюдены</a>
</p>
</footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      randomNumber: 0,
    };
  },
  mounted() {
    this.randomNumber = Math.floor(Math.random() * 100);
  },
};
</script>

<style>
.footer {
  background-color: #25252f;
  margin-top: 2%;
  margin-left: 16%;
  color: white;
  text-align: center;
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
  border-radius: 4px;
}

.newsletter-button {
  padding: 8px 20px;
  border: none;
  border-radius: 4px;
  background-color: #fff;
  color: #2A2A35;
}

.description {
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
  color: white;
  text-decoration: none;
  margin-bottom: 5px;
}

.footer-text {
  background-color: rgba(0, 0, 0, 0.2);
  padding: 10px;
}
</style>  