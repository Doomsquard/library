<template>
  <div class="profilePage">
    <router-view></router-view>
    <profile-component />
    <error-msg />
  </div>
</template>

<script>
import ProfileComponent from "../components/profileComponent.vue";
import ErrorMsg from "../components/errorMsg.vue";

export default {
  name: "profilePage",
  components: { ProfileComponent, ErrorMsg }
};
</script>

<style lang="scss" scoped>
.profilePage {
  height: 100vh;
}
</style>
