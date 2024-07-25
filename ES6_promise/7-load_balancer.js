export default function loadBalancer(chinaDownload, UsDownload) {
  return Promise.race([chinaDownload, UsDownload]);
}
