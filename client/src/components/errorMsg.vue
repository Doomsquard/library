<template>
  <div :class="display" class="error">
    <b-alert show variant="danger">{{ errorMsg }}</b-alert>
  </div>
</template>

<script>
export default {
  name: "errorMsg",
  data() {
    return {
      errorMsg: "",
      display: "none"
    };
  },
  updated() {
    if (this.errorMsg) {
      this.display = "block";
      setTimeout(() => {
        this.display = "none";
        this.$store.dispatch("nullError");
      }, 5000);
    }
  },
  watch: {
    "$store.state.errorMsg": function() {
      this.errorMsg = this.$store.getters["getError"];
    }
  }
};
</script>

<style lang="scss" scoped>
.error {
  z-index: 1;
  top: 50%;
  margin: 0;

  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
  animation: animateErrorBlock 1s ease-in alternate;
  @keyframes animateErrorBlock {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
}
.none {
  display: none;
}
.block {
  display: block;
}
</style>
