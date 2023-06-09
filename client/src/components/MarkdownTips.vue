<template>
    <div class="center">
        <vs-button @click="active = !active" flat style="min-width: 200px" success animation-type="scale">
            <i class='bx bxl-markdown'></i>
            <template #animate>
                Markdown подсказка
            </template>
        </vs-button>
        <vs-dialog scroll overflow-hidden not-close auto-width v-model="active">
            <template #header>
                <h3>
                    Markdown подсказка
                </h3>
            </template>
            <div class="con-content">
                <h2>Заголовки</h2>
                <ul>
                    <li># Заголовок первого уровня</li>
                    <li>## Заголовок второго уровня</li>
                    <li>### Заголовок третьего уровня</li>
                    <li>#### Заголовок четвертого уровня</li>
                    <li>##### Заголовок пятого уровня</li>
                    <li>###### Заголовок шестого уровня</li>
                </ul>
                <h2>Пример</h2>
                <ul>
                    <li>
                        <h1>Заголовок первого уровня</h1>
                    </li>
                    <li>
                        <h2>Заголовок второго уровня</h2>
                    </li>
                    <li>
                        <h3>Заголовок третьего уровня</h3>
                    </li>
                    <li>
                        <h4>Заголовок четвертого уровня</h4>
                    </li>
                    <li>
                        <h5>Заголовок пятого уровня</h5>
                    </li>
                    <li>
                        <h6>Заголовок шестого уровня</h6>
                    </li>
                </ul>
                <hr class="custom-hr">

                <h2>Параграфы и переносы строк</h2>
                Это первая строка. Это вторая строка. Чтобы сделать параграф в конце строки необходимо добавить два пробела.
                <p>Это первая строка</p>
                <p>Это вторая строка</p>
                <hr class="custom-hr">
                <h2>Выделение текста</h2>
                <ul>
                    <li>*курсив*</li>
                    <li>_курсив_</li>
                    <li>**жирный**</li>
                    <li>__жирный__</li>
                    <li>***жирный курсив***</li>
                    <li>___жирный курсив___</li>
                    <li>~~зачеркнутый~~</li>
                </ul>
                <h2>Пример</h2>
                <ul>
                    <li><em>курсив</em></li>
                    <li><em>курсив</em></li>
                    <li><strong>жирный</strong></li>
                    <li><strong>жирный</strong></li>
                    <li><strong><em>жирный курсив</em></strong></li>
                    <li><strong><em>жирный курсив</em></strong></li>
                    <li><s>зачеркнутый</s></li>
                </ul>
                <hr class="custom-hr">

                <h2>Ссылки</h2>
                <p> [Текст ссылки] (https://www.example.com)</p>
                <h2>Пример</h2>
                <p><a href="https://www.example.com">Текст ссылки</a></p>
                <hr class="custom-hr">
                <h2>Изображения</h2>
                <p>![Текст описания] (https://www.example.com/image.jpg)</p>
                <h2>Пример</h2>
                <img src="../assets/img/load/1686147739.7975798_sml1.69841a6.jpg" alt="описание картинки">

            </div>
        </vs-dialog>
    </div>
</template>
<script>
export default {
    data: () => ({
        active: false,
        input1: '',
        input2: '',
        checkbox1: false
    })
}
</script>
<style>
.con-content p {
    margin: 20px 0px;
    position: relative;
    display: block;
    font-size: .9rem;
}

.custom-hr {
    border-color: black;
}
</style>



