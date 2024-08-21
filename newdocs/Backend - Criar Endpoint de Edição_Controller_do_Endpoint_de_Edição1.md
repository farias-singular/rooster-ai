```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.UpdateBrand
{
    [Route("api/organizations/{organizationId}/brands/{id}")]
    [ApiController]
    [ApiExplorerSettings(GroupName = "Brands")]
    public class UpdateBrandController : Controller
    {
        /// <summary>
        /// Updates an existing Brand in the Organization tenant after an authorized client request.
        /// </summary>
        /// <param name="organizationId"></param>
        /// <param name="id"></param>
        /// <param name="request"></param>
        /// <param name="mediator"></param>
        /// <returns></returns>
        [HttpPut]
        [Authorize]
        [ProducesResponseType(typeof(UpdateBrandDto), StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        [ProducesResponseType(StatusCodes.Status401Unauthorized)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [ProducesResponseType(StatusCodes.Status503ServiceUnavailable)]
        public async Task<IActionResult> UpdateBrand(
            [FromRoute] string organizationId, 
            [FromRoute] string id,
            [FromBody] UpdateBrandRequest request, 
            [FromServices] IMediator mediator)
        {
            var command = new UpdateBrandCommand(
                id: id,
                organizationId: organizationId,
                categoryId: request.CategoryId,
                name: request.Name,
                title: request.Title);

            var response = await mediator.Send(command);

            return Ok(response);
        }
    }
}
```