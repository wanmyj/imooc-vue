export function isExternal (path) {
  console.info(/^(https?:|mailto:|tel:)/.test(path) ? "external" : "internal")
  return /^(https?:|mailto:|tel:)/.test(path)
}
