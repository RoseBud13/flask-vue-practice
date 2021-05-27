import request from '../utils/request'


// -----------------------------------------------Resources----------------------------------------

export function fetchResources(query) {
  return request({
    url: '/resources/',
    method: 'get',
    params: query
  })
}

export function addResource(data) {
  return request({
    url: '/resources/',
    method: 'post',
    data
  })
}

export function getResource(id) {
  return request({
    url: `/resources/${id}/`,
    method: 'get'
  })
}

export function deleteResource(id) {
  return request({
    url: `/resources/${id}/`,
    method: 'delete'
  })
}

export function updateResource(id, data) {
  return request({
    url: `/resources/${id}/`,
    method: 'put',
    data
  })
}

// -----------------------------------------------Reservations----------------------------------------

export function fetchReservations(query) {
  return request({
    url: `/reservations/`,
    method: 'get',
    params: query
  })
}

export function addReservation(data) {
  return request({
    url: `/reservations/`,
    method: 'post',
    data
  })
}

export function getReservation(id) {
  return request({
    url: `/reservations/${id}/`,
    method: 'get'
  })
}

export function updateReservation(id, data) {
  return request({
    url: `/reservations/${id}/`,
    method: 'put',
    data
  })
}

export function cancelReservation(id) {
  return request({
    url: `/reservations/${id}/`,
    method: 'delete'
  })
}
