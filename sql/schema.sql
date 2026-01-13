create table cellule (
   id_cellule  int primary key,
   nom_cellule varchar(50) not null
);

create table membre (
   id_membre   int primary key,
   nom         varchar(50) not null,
   prenom      varchar(50) not null,
   email       varchar(100),
   type_membre varchar(20), -- 'admin', 'chef', 'membre'
   id_cellule  int,
   foreign key ( id_cellule )
      references cellule ( id_cellule )
);

create table evenement (
   id_evenement   int primary key,
   titre          varchar(100) not null,
   date_evenement date,
   lieu           varchar(100)
);

create table participation (
   id_participation int primary key,
   id_membre        int,
   id_evenement     int,
   statut           varchar(20), -- exemple : 'présent', 'absent', 'invité'
   foreign key ( id_membre )
      references membre ( id_membre ),
   foreign key ( id_evenement )
      references evenement ( id_evenement )
);

create table message (
   id_message      int primary key,
   contenu         text not null,
   date_envoi      datetime,
   id_expediteur   int,
   id_destinataire int,
   foreign key ( id_expediteur )
      references membre ( id_membre ),
   foreign key ( id_destinataire )
      references membre ( id_membre )
);

create table contact (
   id_contact  int primary key,
   nom_contact varchar(100) not null,
   email       varchar(100),
   telephone   varchar(20),
   id_cellule  int,
   foreign key ( id_cellule )
      references cellule ( id_cellule )
);