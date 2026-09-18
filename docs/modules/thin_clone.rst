.. _thin_clone_module:


thin_clone -- Create Thin Clones on Dell PowerFlex 5.x (Gen2)
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Creates a thin clone from a source volume (including an existing thin clone, which is itself a volume) or from a read-only snapshot on a PowerFlex 5.x Gen2 storage system. This module is CREATION-ONLY. Ongoing management of the resulting thin clone (rename, resize, map/unmap, delete) is the responsibility of the M(dellemc.powerflex.volume) module, following the PowerFlex Gen2 architecture pattern: System creates, Volume manages. Supported on PowerFlex 5.0 and above only.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

 from_volume_name (optional, str, None)
    Name of the source volume (or source thin clone).

    Mutually exclusive with :emphasis:`from\_volume\_id`\ , :emphasis:`from\_snapshot\_name`\ , and :emphasis:`from\_snapshot\_id`.


 from_volume_id (optional, str, None)
    ID of the source volume (or source thin clone).

    Mutually exclusive with :emphasis:`from\_volume\_name`\ , :emphasis:`from\_snapshot\_name`\ , and :emphasis:`from\_snapshot\_id`.


 from_snapshot_name (optional, str, None)
    Name of the source (read-only) snapshot.

    Mutually exclusive with :emphasis:`from\_snapshot\_id`\ , :emphasis:`from\_volume\_name`\ , and :emphasis:`from\_volume\_id`.


 from_snapshot_id (optional, str, None)
    ID of the source (read-only) snapshot.

    Mutually exclusive with :emphasis:`from\_snapshot\_name`\ , :emphasis:`from\_volume\_name`\ , and :emphasis:`from\_volume\_id`.


 new_clone_name (True, str, None)
    Name of the new thin clone volume to create.

    Required. Must be non-empty.


 state (optional, str, present)
    Desired state. This module supports :literal:`present` only.

    Delete, rename, resize, and mapping are handled by :literal:`dellemc.powerflex.volume\_v2`.

    Choices: present


 hostname (True, str, None)
    IP or FQDN of the PowerFlex host.


 username (True, str, None)
    The username of the PowerFlex host.


 password (True, str, None)
    The password of the PowerFlex host.


 validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    :literal:`true` - Indicates that the SSL certificate should be verified.

    :literal:`false` - Indicates that the SSL certificate should not be verified.


 port (optional, int, 443)
    Port number through which communication happens with PowerFlex host.


 timeout (optional, int, 120)
    Time after which connection will get terminated.

    It is to be mentioned in seconds.




Notes
-----

.. note::
   - Requires PowerFlex 5.0 or later.
   - Architecture: System creates, Volume manages. Use :literal:`dellemc.powerflex.volume\_v2` for rename, resize, map/unmap, delete, and other ongoing operations on the returned thin clone.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create thin clone from a source volume
      dellemc.powerflex.thin_clone:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        from_volume_name: "src_vol"
        new_clone_name: "clone_a"
        state: present

    - name: Create thin clone from a read-only snapshot
      dellemc.powerflex.thin_clone:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        from_snapshot_name: "src_snap"
        new_clone_name: "clone_b"
        state: present



Return Values
-------------

changed (always, bool, )
  Whether a new thin clone was created.


volume_details (always, dict, )
  Details of the thin clone volume.


source_details (always, dict, )
  Resolved source used for the create operation.





Status
------

This module is supported on Dell PowerFlex 5.x and later versions.



Authors
~~~~~~~

- Dell Technologies Ansible Team (@dell-ansible)
