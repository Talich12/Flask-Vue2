import { unref as N } from "vue";
const T = "https://www.youtube-nocookie.com", R = "https://www.youtube.com", L = "vue-youtube";
var _ = /* @__PURE__ */ ((O) => (O[O.INVALID_PARAMETER = 2] = "INVALID_PARAMETER", O[O.HTML5_ERROR = 5] = "HTML5_ERROR", O[O.NOT_FOUND = 100] = "NOT_FOUND", O[O.NOT_ALLOWED = 101] = "NOT_ALLOWED", O[O.NOT_ALLOWED_DISGUISE = 150] = "NOT_ALLOWED_DISGUISE", O))(_ || {}), I = /* @__PURE__ */ ((O) => (O[O.UNSTARTED = -1] = "UNSTARTED", O[O.ENDED = 0] = "ENDED", O[O.PLAYING = 1] = "PLAYING", O[O.PAUSED = 2] = "PAUSED", O[O.BUFFERING = 3] = "BUFFERING", O[O.VIDEO_CUED = 5] = "VIDEO_CUED", O))(I || {});
function u(O) {
  var E;
  const D = N(O);
  return (E = D == null ? void 0 : D.$el) != null ? E : D;
}
export {
  R as HOST_COOKIE,
  T as HOST_NO_COOKIE,
  L as PROVIDE_KEY,
  _ as PlayerError,
  I as PlayerState,
  u as unrefElement
};
