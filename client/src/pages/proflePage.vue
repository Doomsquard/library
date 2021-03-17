<template>
  <div class="profilePage">
    <router-view></router-view>
    <profile-component />
  </div>
</template>

<script>
import ProfileComponent from "../components/profileComponent.vue";

export default {
  name: "profilePage",
  components: { ProfileComponent }
};
</script>

<style lang="scss" scoped>
.profilePage {
  height: 100vh;
}
</style>
