# A script that installs puppet-lint package.
package { 'puppet-lint':
  ensure   => '2.5',
  provider =>  'gem'
}
