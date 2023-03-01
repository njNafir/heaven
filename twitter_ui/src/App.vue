<template>
  <div class="bg-gray-300 flex flex-col h-screen">
    <Header />
    <div class="p-8 w-3/4 mx-auto bg-white flex-1">
      <Tweets />
    </div>
  </div>
</template>

<script>
import Tweets from "./components/Tweets.vue";
import Header from "./components/Header.vue";
export default {
  name: "App",
  components: {
    Tweets,
    Header
  }
};
</script>