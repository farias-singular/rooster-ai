```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.DeleteBrand
{
    [Route("api/organizations/{organizationId}/brands/{id}")]
    [ApiController]
    [ApiExplorerSettings(GroupName = "Brands")]
    public class DeleteBrandController : Controller
    {
        /// <summary>
        /// Deletes an existing Brand in the Organization tenant after an authorized client request.
        /// </summary>
        /// <param name="organizationId"></param>
        /// <param name="id"></param>
        /// <param name="mediator"></param>
        /// <returns></returns>
        [HttpDelete]
        [Authorize]
        [ProducesResponseType(StatusCodes.Status204NoContent)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        [ProducesResponseType(StatusCodes.Status401Unauthorized)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [ProducesResponseType(StatusCodes.Status503ServiceUnavailable)]
        public async Task<IActionResult> DeleteBrand(
            [FromRoute] string organizationId, 
            [FromRoute] string id,
            [FromServices] IMediator mediator)
        {
            var command = new DeleteBrandCommand(
                id: id,
                organizationId: organizationId);

            await mediator.Send(command);

            return NoContent();
        }
    }
}
```