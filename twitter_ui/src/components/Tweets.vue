<template>
  <div>
    <div class="text-2xl text-blue-400 mb-5">Realtime Dev Tweets</div>
    <div
      v-for="tweet in tweets"
      :key="tweet.id"
      class="border-2 border-blue-400 p-1 mb-4 shadow rounded"
    >
      <div class="flex mb-2">
        <div class="mr-2">
          <img :src="tweet.user.profile_image_url" alt="" class="rounded">
        </div>
        <div class="font-semibold text-xl">{{ tweet.user.screen_name }}</div>
      </div>
      <div>{{ tweet.text }}</div>
      <div class="flex mt-2">
        <div class="mr-5"><span class="font-semibold">{{ tweet.user.friends_count }}</span> Following</div>
        <div class="mr-5"><span class="font-semibold">{{ tweet.user.followers_count }}</span> Followers</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tweets",
  data() {
    return {
      tweets: [],
      connection: null
    };
  },
  mounted() {
    this.connection = new WebSocket("ws://localhost:8088");
    this.connection.onmessage = event => {
      if (this.tweets.length >= 20) {
        this.tweets.pop();
      }
      this.tweets.unshift(JSON.parse(event.data));
      // this.tweets.push(JSON.parse(event.data));
    };
    this.connection.onopen = function(event) {
      console.log(event);
    };
  }
};
</script>