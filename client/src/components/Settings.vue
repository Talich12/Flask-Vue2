<template>
  <div class="center">
    <vs-button danger size="large" shadow @click="active = !active">
      <i class='bx bxs-wrench'></i> Настройки уведомлений
    </vs-button>
    <vs-dialog blur v-model="active">
      <template #header>
        <h4 class="not-margin">
          Настройки уведомлений
        </h4>
      </template>
      <div class="con-form">
        <div class="con-not">
          <div class="notification-all">
            <div class="column">
              <span class="not-email">Уведомления по электронной почте</span>
              <span class="not-com">Вашу историю прокомментировали</span>
              <span class="not-like">Ваша история понравилась</span>
              <span class="not-answer">На ваш комментарий ответили</span>
              <span class="not-newSub">У вас новый читатель</span>
              <span class="not-newHis">Новая история</span>
            </div>
            <div class="column-switch">
              <!--  <vs-switch danger v-model="notification1" class="not_email"></vs-switch>-->
              <vs-switch danger style="background-color: rgb(203, 201, 201);" v-model="active5">
                <template #off>
                  <i class='bx bx-x'></i>
                </template>
                <template #on>
                  <i class='bx bx-check'></i>
                </template>
              </vs-switch>
              <vs-switch danger style="background-color: rgb(203, 201, 201);" v-model="active5">
                <template #off>
                  <i class='bx bx-x'></i>
                </template>
                <template #on>
                  <i class='bx bx-check'></i>
                </template>
              </vs-switch>
              <vs-switch danger style="background-color: rgb(203, 201, 201);" v-model="active5">
                <template #off>
                  <i class='bx bx-x'></i>
                </template>
                <template #on>
                  <i class='bx bx-check'></i>
                </template>
              </vs-switch>
              <vs-switch danger style="background-color: rgb(203, 201, 201);" v-model="active5">
                <template #off>
                  <i class='bx bx-x'></i>
                </template>
                <template #on>
                  <i class='bx bx-check'></i>
                </template>
              </vs-switch>
              <vs-switch danger style="background-color: rgb(203, 201, 201);" v-model="active5">
                <template #off>
                  <i class='bx bx-x'></i>
                </template>
                <template #on>
                  <i class='bx bx-check'></i>
                </template>
              </vs-switch>
              <vs-switch danger style="background-color: rgb(203, 201, 201);" v-model="active5">
                <template #off>
                  <i class='bx bx-x'></i>
                </template>
                <template #on>
                  <i class='bx bx-check'></i>
                </template>
              </vs-switch>
            </div>
          </div>


         
        </div>

      </div>

    </vs-dialog>
  </div>
</template>
<script>
export default {
  data: () => ({
    active: false,

  })
}
</script>
<style>
.not-margin {
  margin: 0;
  font-weight: normal;
  padding: 10px;
}

.con-form {
  width: 100%;
}

.con-form .flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.con-form .flex a {
  font-size: 0.8rem;
  opacity: 0.7;
}

.notification-all {
  display: flex;
  justify-content: space-between;
  white-space: nowrap;

}

.column {
  display: flex;
  flex-direction: column;

}

.column-switch {
  display: flex;
  flex-direction: column;
  margin-left: 2%;

}

.vs-switch {
  margin-bottom: 13%;
}

span {
  margin: 2%;
}

.not-email,
.not-com,
.not-like,
.not-answer,
.not-newSub,
.not-newHis {
  margin-bottom: 10px;
}
</style>
