<template>
  <div class="libraryPage">
    <router-view></router-view>
    <library-component />
  </div>
</template>

<script>
import libraryComponent from "../components/libraryComponent";

export default {
  name: "libraryPage",
  components: { libraryComponent }
};
</script>

<style lang="scss" scoped>
.libraryPage {
  height: 100vh;
}
</style>
