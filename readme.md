
# Script para generación y crop de imágenes con formatos preestablecidos (alta, media, baja) con criterios de modelo OpenCV


## Motivación

Para plataformas que se necesite tener imágenes en múltiples formatos (alta, media baja), es engorroso tener que dedicarle mucho tiempo a un proceso que podría hacerse manual. El problema de automatizar el cropeo o recorte de fotos es que si se automatiza sin criterio, se puede llegar a obtener resultados que no favorecen el output (por ejemplo incluyendo en la zona de corte cosas que no son de interés o que hubiese sido mejor un corte diferente incluyendo objetos identificables como casas, obras, personas, carteles). 

La idea de este pequeño proyecto es poder automatizar el corte de fotos con algún criterio de detección de objetos o valoración de los objetos para la zona de corte.

Para esto se encontraron 2 librerías y estos scripts simplemente automatizan la ejecución de dichas librerías.

Se realizaron pruebas con ambas librerías, obteniendo mejores resultados con la versión 1 del script publicado en dicho repo.





