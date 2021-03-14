<template>
  <div class="signIn">
    <router-view></router-view>
    <sign-component />
  </div>
</template>

<script>
import signComponent from "../components/signComponent";

export default {
  components: { signComponent },
  name: "signInpage"
};
</script>

<style lang="scss" scoped>
.signIn {
  min-height: 100vh;
  background-color: #f5f5f5;
}
</style>
