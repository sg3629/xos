'use strict';

angular.module('xos.synchronizerNotifier', [
  'ngResource',
  'ngCookies',
  'ui.router',
  'xos.helpers'
])
.service('Diag', function($rootScope, $http, $q, $interval){

  let isRunning = false;

  this.getDiags = () => {
    let d = $q.defer();
    $http.get('/api/core/diags')
    .then(res => {
      d.resolve(res.data);
    })
    .catch(err => {
      d.reject(err);
    });

    return d.promise;
  };

  this.sendEvents = (diags) => {
    diags.forEach(d => {
      let status = JSON.parse(d.backend_register);
      status.last_run = new Date(status.last_run * 1000);
      status.last_duration = status.last_duration * 1000;
      status.last_synchronizer_start = new Date(status.last_synchronizer_start * 1000);
      status.last_syncrecord_start = status.last_syncrecord_start ? new Date(status.last_syncrecord_start * 1000) : null;
      $rootScope.$broadcast(`diag`, {
        name: d.name,
        updated: d.updated,
        info: status,
        status: this.getSyncStatus(status)
      });
    });
  };

  this.start = () => {
    isRunning = true;
    this.getDiags()
    .then(diags => {
      this.sendEvents(diags);
    });
    return isRunning;
  };

  this.stop = () => {
    isRunning = false;
    return isRunning;
  };

  this.getSyncStatus = (status) => {

    const now = new Date();
    // let gap = 15 * 60 * 1000; /* ms */
    const gap = 1 * 60 * 1000;
    // if all of this values are older than 15 min,
    // probably something is wrong
    if (
      (now - status.last_synchronizer_start) > gap &&
      (now - status.last_syncrecord_start) > gap &&
      (now - status.last_run) > gap
    ){
      return false;
    }
    else{
      return true;
    }
  }

  $interval(() => {
    if(isRunning){
      this.getDiags()
      .then(diags => {
        this.sendEvents(diags);
      });
    }
  }, 10000);
})
.directive('syncStatus', function() {
  return {
    restrict: 'E',
    scope: {},
    bindToController: true,
    controllerAs: 'vm',
    templateUrl: 'templates/sync-status.tpl.html',
    controller: function($log, $rootScope, Diag, xosNotification){
      Diag.start();
      this.showNotificationPanel = true;
      this.synchronizers = {};

      const notified = {};

      this.showNoSync = true;

      $rootScope.$on('diag', (e, d) => {
        this.synchronizers[d.name] = d;

        // if errored
        if(!d.status){
          // and not already notified
          if(!notified[d.name]){
            xosNotification.notify('CORD Synchronizer Error', {
              icon: '/xos/core/static/cord-logo.png',
              body: `The ${d.name} synchronizer has stopped.`
            });
          }
          notified[d.name] = true;
        }
        else {
          notified[d.name] = false;
        }

        // hide list if empty
        this.showNoSync = false;
        if(Object.keys(this.synchronizers).length === 0){
          this.showNoSync = true;
        }
      });

    }
  }
});

angular.element(document).ready(function() {
  angular.bootstrap('#xosSynchronizerNotifier', ['xos.synchronizerNotifier']);
});