<template>
    <vs-card style="margin-top: 10%;">
        <template #title>
            <h3><slot name="title"></slot></h3>
        </template>
        <template #img>

            <slot name="img"></slot>
        </template>
        <template #text>
        <p>
            <slot name="text"></slot>
        </p>
        </template>
        <template #interactions>
        <vs-button danger icon>
            <i class='bx bx-heart'></i>
        </vs-button>
        <vs-button class="btn-chat" shadow primary>
            <i class='bx bx-chat' ></i>
            <span class="span">
            54
            </span>
        </vs-button>
        </template>
    </vs-card>
</template>

<script>
export default {
 
}
</script>