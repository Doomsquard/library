<template>
  <div class="booksPage">
    <router-view></router-view>
    <books-component />
  </div>
</template>

<script>
import BooksComponent from "../components/booksComponent.vue";

export default {
  name: "booksPage",
  components: { BooksComponent }
};
</script>

<style lang="scss" scoped>
.booksPage {
  height: 100vh;
}
</style>
